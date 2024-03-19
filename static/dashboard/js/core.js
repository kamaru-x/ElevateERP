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

    $('#first_payment, #service').on('keyup change paste', function() {
        var first_payment = $('#first_payment').val() || 0
        var service = $('#service').val() || 0

        var collage_payment = parseFloat(first_payment) - parseFloat(service)

        $('#collage_payment').val(parseFloat(collage_payment))
    });

    // $('#transaction_type').on('change',function(){
    //     var type = $('#transaction_type').val()

    //     $.ajax({
    //         url : '/Accounts/get/entry-categories/',
    //         type : 'POST',
    //         data : {'type':type},

    //         success : function(response){
    //             html = '<option value="">Select Category</option>'
    //             categories = response.categories 
    //             for (let i = 0; i < response.categories.length; i++) {
    //                 html += '<option value="'+categories[i].CATID+'">'+categories[i].Title+'</option>'
    //             }

    //             $('#entry_category').html(html)
    //         }
    //     })
    // })

    $('#entry_category').on('change',function(){
        var id = $('#entry_category').val()

        $.ajax({
            url : '/Accounts/get/fot/',
            type : 'POST',
            data : {'id':id},

            success : function(response){
                if(response.fot == 'STUDENT'){
                    $('#students-div').show();
                    $('#staffs-div, #collages-div, #main-agents-div, #sub-agents-div, #title-div, #amount-div').hide();
                }else if(response.fot == 'COLLAGE'){
                    $('#collages-div').show();
                    $('#staffs-div, #students-div, #main-agents-div, #sub-agents-div, #title-div, #amount-div').hide();
                }else if(response.fot == 'STAFF'){
                    $('#staffs-div').show();
                    $('#collages-div, #students-div, #main-agents-div, #sub-agents-div, #title-div, #amount-div').hide();
                }else if(response.fot == 'SUBAGENT'){
                    $('#sub-agents-div').show();
                    $('#collages-div, #students-div, #main-agents-div, #staffs-div, #title-div, #amount-div').hide();
                }else if(response.fot == 'MAINAGENT'){
                    $('#main-agents-div').show();
                    $('#collages-div, #students-div, #sub-agents-div, #staffs-div, #title-div, #amount-div').hide();
                }else if(response.fot == 'OTHER'){
                    $('#title-div, #amount-div').show();
                    $('#collages-div, #students-div, #main-agents-div, #staffs-div, #sub-agents-div').hide();
                }
            }
        })
    })

    $('#student, #staff, #collage, #main_agent, #sub_agent').on('change' , function(){
        $('#amount-div').show()
        $('#title-div').show()
    })
})