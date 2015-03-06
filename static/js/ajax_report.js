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

    // debug
      //console.log(data);

    // csv report
      if (data.csv_created) var csv_report = '<div>A comprehensive report can be reviewed within <a href="/static/csv/login_activity.csv">logic_activity.csv</a></div>';

    // login counts
      var login_counts = '<div class="login-counts">';
        login_counts += '<div>Login Count (30 days): ' + data.report.total_30 + '</div>';
        login_counts += '<div>Login Count (60 days): ' + data.report.total_60 + '</div>';
        login_counts += '<div>Login Count (90 days): ' + data.report.total_90 + '</div>';
        login_counts += '</div>';

    // login percentages
      var login_percentages = '<div class="login-percentages">';
        login_percentages += '<div>Login Percentage (30 days): ' + (data.report.percentage_30 * 100).toFixed(2) + '%</div>';
        login_percentages += '<div>Login Percentage (60 days): ' + (data.report.percentage_60 * 100).toFixed(2) + '%</div>';
        login_percentages += '<div>Login Percentage (90 days): ' + (data.report.percentage_90 * 100).toFixed(2) + '%</div>';
        login_percentages += '</div>';

    // remove previous report
       $('.report').remove()

    // append report to dom
       $('body').append('<div class="report">' + csv_report + login_counts + login_percentages + '</div>');
    });

  // AJAX Failure
    ajax_report.fail(function(jqXHR, textStatus, errorThrown) {
      console.log('Error Thrown: '+errorThrown);
      console.log('Error Status: '+textStatus);

      $('.ajax_overlay').fadeOut(200, function(){ $(this).remove() });
    });

  });
});
