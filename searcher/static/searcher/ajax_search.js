var user_input = $(".search-input");
var softwares_div = $("#ajax-software-search-replace");
var endpoint = "/searcher/";
var delay_by_in_ms = 700;
let scheduled_function = false;

let ajax_call = function (endpoint, request_parameters) {
  $.getJSON(endpoint, request_parameters).done((response) => {
    softwares_div
      .fadeTo("slow", 0)
      .promise()
      .then(() => {
        // replace the HTML contents
        softwares_div.html(response["html_from_view"]);
        // fade-in the div with new contents
        softwares_div.fadeTo("slow", 1);

        addEventClickToItems();
      });
  });
};

user_input.on("keyup", function () {
  var request_parameters = {
    s: $(this).val(),
  };

  if (scheduled_function) {
    clearTimeout(scheduled_function);
  }

  scheduled_function = setTimeout(
    ajax_call,
    delay_by_in_ms,
    endpoint,
    request_parameters
  );
});
