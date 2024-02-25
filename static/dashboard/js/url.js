// $(document).ready(function(){
//     $('#title').on('keyup',function(){
//         var value = $('#title').val();
//         var final = value.replace(/ /g,"-");
//         $('#url').val(final);
//     });
// })

$(document).ready(function(){
    $('#title').on('keyup', function(){
        var value = $('#title').val();
        var final = value.replace(/[^\w\s-]/g, '-'); // Replace non-word characters except spaces and hyphens with hyphens
        final = final.replace(/\s+/g, '-'); // Replace spaces with hyphens
        final = final.replace(/-+/g, '-'); // Replace consecutive hyphens with a single hyphen
        final = final.replace(/\//g, '-'); // Replace slashes with hyphens
        $('#url').val(final);
    });
});