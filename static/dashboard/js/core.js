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

    $('#total, #service').on('keyup change paste', function() {
        var total = $('#total').val() || 0
        var service = $('#service').val() || 0

        var collage_payment = parseFloat(total) - parseFloat(service)

        $('#collage_payment').val(parseFloat(collage_payment))
    });

    $('#transaction_type').on('change',function(){
        var type = $('#transaction_type').val()

        $.ajax({
            url : '/Accounts/get/entry-categories/',
            type : 'POST',
            data : {'type':type},

            success : function(response){
                html = '<option value="">Select Category</option>'
                categories = response.categories 
                for (let i = 0; i < response.categories.length; i++) {
                    html += '<option value="'+categories[i].CATID+'">'+categories[i].Title+'</option>'
                }

                $('#entry_category').html(html)
            }
        })
    })

    $('#entry_category').on('change',function(){
        var catid = $('#entry_category').val()
        if (catid == 'SFPTOES'){
            $('#students-div').show()
        }else if(catid == 'SLRY'){
            $('#staff-div').show()
        }

        $('#title-div').show()
        $('#amount-div').show()
    })
})