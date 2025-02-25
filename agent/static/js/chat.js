$(document).ready(function() {

  var messages = $("#chat-messages");

  function addMessage(text, source) {
    var message = $("<div class='chat-message " + source + "'><p>" + text + "</p></div>");
    messages.append(message);
    messages.scrollTop(messages[0].scrollHeight);
  }

  // Bind the logout action
  $("#logout").click(function(e) {
    e.preventDefault();
    $("#logoutForm").submit();
    return false;
  });

  // Bind keypresses to the chat input
  $("#promptInput").keypress(function(e) {
    if (e.keyCode == 13 && !e.shiftKey) {
      e.preventDefault();
      $("#chatForm").submit();
      return false;
    }
  });

  // Bind the submit action
  $("#chatForm").submit(function(e) {
    e.preventDefault();
    var ta = $("#promptInput");
    var prompt = ta.val();

    if (prompt.length > 0) {
      ta.val('');
      addMessage(prompt, 'user');

      let csrf = $('input[name="csrfmiddlewaretoken"]').val();
      $.ajax({
        type: "POST",
        url: "/chat/prompt",
        headers: {
          "X-CSRFToken": csrf
        },
        data: {prompt: prompt},
        success: function(data) {
          addMessage(data.summary, 'agent');
        }
      });
    }
    return false;
  });

});