$(document).ready(function() {
    $("#show_after_submit1").hide();
    $("#show_after_submit2").hide();

    jQuery.validator.setDefaults({
        success: "valid"
    });

    $("#input_form").validate({
        rules: {
            field: {
                required: true,
                url: true
            }
        },
        submitHandler: function(form) {
            $("#hide_after_submit").hide();
            $("#show_after_submit1").show();
            $("#show_after_submit2").show();
            form.submit();
        }
    });
});

