$(document).ready(function() {
  $("#btn_translate").click(translateHello);
  $("#language_code").on("keypress", function(event) {
    if (event.key === "Enter") {
      translateHello();
    }
  });

  function translateHello() {
    var languageCode = $("#language_code").val().trim();
    var apiUrl = "https://www.fourtonfish.com/hellosalut/hello/" + languageCode;

    $.ajax({
      url: apiUrl,
      dataType: 'json',
      success: function(response) {
        if (response && response.hello) {
          $("#hello").text(response.hello);
        } else {
          $("#hello").text("Translation not found.");
        }
      },
      error: function(xhr, status, error) {
        $("#hello").text("Error fetching translation.");
        console.error("Error:", error);
      }
    });
  }
});
