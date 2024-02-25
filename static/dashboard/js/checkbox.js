$(document).ready(function(){
    var show_price = $("#show_price").is(":checked");
    var order_whatsapp = $('#order_whatsapp').is(":checked");
    
    // Output the result
    if (show_price) {
        $('#actual_price').show()
        $('#offer_price').show()
    } else {
        $('#actual_price').hide()
        $('#offer_price').hide()
    }

    if (order_whatsapp) {
        $('#code').show()
        $('#whatsapp').show()
    } else {
        $('#code').hide()
        $('#whatsapp').hide()
    }

    $('#show_price').on('change', function() {
        var show_price = $(this).is(":checked");
        
        if (show_price) {
            $('#actual_price').show();
            $('#offer_price').show();
        } else {
            $('#actual_price').hide();
            $('#offer_price').hide();
        }
    });

    $('#order_whatsapp').on('change', function() {
        var order_whatsapp = $(this).is(":checked");
        
        if (order_whatsapp) {
            $('#code').show();
            $('#whatsapp').show();
        } else {
            $('#code').hide();
            $('#whatsapp').hide();
        }
    });
})