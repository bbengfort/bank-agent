# Bank Agent

The purpose of this application is to allow security research into Generative AI to
discover vulnerabilities or secure best practices for function calling LLMs;
particularly those that use HTTP APIs to make requests.

This application has two primary web services:

1. Bank: an API that mimicks a bank service where you can list accounts, balances, and make transfers both between your own accounts and other accounts.
2. Agent: a Generative AI agent that can interact with the Bank API on the user's behalf.