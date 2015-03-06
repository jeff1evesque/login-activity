/**
 * ajax_report.js: this script utilizes ajax to retrieve login-activity
 *                 report to the current webpage.
 */

$(document).ready(function() {
  $('.btn-generateReport').on('click', function(event) {
    event.preventDefault();

  // AJAX Process
    var ajax_report = $.ajax({
      type: 'POST',
      url: '/generate-report/',
      dataType: 'json',
      beforeSend: function() {
        ajaxLoader( $('body') );
      }
    });

  // AJAX Success
    ajax_report.done(function(data) {
      $('.ajax_overlay').fadeOut(200, function(){ $(this).remove() });
    });

  // AJAX Failure
    ajax_report.fail(function(jqXHR, textStatus, errorThrown) {
      console.log('Error Thrown: '+errorThrown);
      console.log('Error Status: '+textStatus);

      $('.ajax_overlay').fadeOut(200, function(){ $(this).remove() });
    });

  });
});
