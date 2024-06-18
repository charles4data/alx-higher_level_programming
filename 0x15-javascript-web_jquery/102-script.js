document.addEventListener('DOMContentLoaded', function() {
  $('#btn_translate').click(function() {
    const langCode = $('#language_code').val();

    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/?lang=${langCode}`,
      dataType: 'json',
      success: function(data) {
        $('#hello').text(data.hello); 
      },
      error: function() {
        $('#hello').text('Error fetching translation');
      }
    });
  });
});
