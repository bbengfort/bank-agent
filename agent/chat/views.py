from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView

from chat.bank import list_accounts, account_balance, transfer_funds

from vertexai.generative_models import (
    Content,
    FunctionDeclaration,
    GenerationConfig,
    GenerativeModel,
    Part,
    Tool,
    ToolConfig,
)


class ChatUI(TemplateView):

    template_name = "chat.html"


class Prompt(APIView):

    def post(self, request):
        prompt = request.data.get("prompt")
        if prompt is None or len(prompt) < 2:
            return Response({"message": "Invalid prompt"}, status=400)

        list_accounts_func = FunctionDeclaration.from_func(list_accounts)
        account_balance_func = FunctionDeclaration.from_func(account_balance)
        transfer_funds_func = FunctionDeclaration.from_func(transfer_funds)

        user_prompt_content = Content(
            role="user",
            parts=[
                Part.from_text(prompt),
            ],
        )

        model = GenerativeModel(model_name="gemini-2.0-flash-001")
        tools = Tool(
            function_declarations=[
                list_accounts_func, account_balance_func, transfer_funds_func,
            ]
        )

        response = model.generate_content(
            user_prompt_content,
            generation_config=GenerationConfig(temperature=0),
            tools=[tools],
            tool_config=ToolConfig(
                function_calling_config=ToolConfig.FunctionCallingConfig(
                    mode=ToolConfig.FunctionCallingConfig.Mode.ANY,
                    allowed_function_names=[
                        "list_accounts", "account_balance", "transfer_funds",
                    ],
                )
            )
        )

        funcs = {
            "list_accounts": list_accounts,
            "account_balance": account_balance,
            "transfer_funds": transfer_funds,
        }

        fc = response.candidates[0].function_calls[0]
        value = funcs[fc.name](*fc.args)

        response = model.generate_content(
            [
                user_prompt_content,
                response.candidates[0].content,
                Content(
                    parts=[
                        Part.from_function_response(
                            name=fc.name,
                            response={"content": value}
                        )
                    ]
                )
            ],
            tools=[tools],
        )

        return Response({"summary": response.text})
