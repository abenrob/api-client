$(function() {
	var viewDaJSON = function(json){
    	var container = document.getElementById('daOutput');
		var options = {
			mode: 'view'
		};
		var editor = new jsoneditor.JSONEditor(container, options, json);
    };
    var make_call = function(e) {
    	$('#daOutput').empty();
		$.getJSON($SCRIPT_ROOT + '/_callAPI', {
			uri: $('#daURI').val(),
			params: $('#daParams').val().toString(),
			username: $('#userName').val(),
			password: $('#userPassword').val()
		}, function(data) {
			viewDaJSON(data);
		});
		return false;
    };
    
    $('#goGetIt').bind('click', make_call);
    $('#daURI').focus();
  });