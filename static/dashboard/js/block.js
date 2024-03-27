$("#FilUploader").change(function () {
    var fileExtension = ['jpg' , 'jpeg' , 'jfif ', 'pjpeg' , 'pjp','png','webp'];
    if ($.inArray($(this).val().split('.').pop().toLowerCase(), fileExtension) == -1) {
        alert("Only formats are allowed : "+fileExtension.join(', '));
        $("#FilUploader").val('');
    }
});