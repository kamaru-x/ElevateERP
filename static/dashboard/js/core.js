$(document).ready(function(){
    $('#course').on('change',function(){
        var course_id = $('#course').val()
        
        $.ajax({
            url : '/get/addons/',
            type : 'POST',
            data : {'course_id':course_id},

            success : function(response){
                html = '<option value="">Select Addon</option>'
                addons = response.addons 
                for (let i = 0; i < response.addons.length; i++) {
                    html += '<option value="'+addons[i].id+'">'+addons[i].Title+'</option>'
                }

                $('#addons').html(html)
            }
        })
    })

    $('#fees, #donation, #discount').on('keyup change paste', function() {
        var fees = $('#fees').val() || 0
        var donation = $('#donation').val() || 0
        var discount = $('#discount').val() || 0

        total = parseFloat(fees) + parseFloat(donation) - parseFloat(discount)

        $('#total').val(parseFloat(total))
    });
})