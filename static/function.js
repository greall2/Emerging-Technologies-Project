var reader  = new FileReader();

var files_allwd = ['gif','png','jpg','jpeg'];


function upload_file(){
    // Adapted from: https://stackoverflow.com/questions/651700/how-to-have-jquery-restrict-file-types-on-upload
    var file_name = $('#input_file');
    var ext = file_name.val().split('.').pop().toLowerCase();
    if ($(file_name).get(0).files.length === 0) {
        alert("No files selected.");
        return;
    }else if($.inArray(ext, files_allwd) == -1) {
        alert('Must be .jpg, .png or .gif format.');
        return;
    }
    //https://developer.mozilla.org/en-US/docs/Web/API/FileReader/readAsDataURL
    var file = document.querySelector('input[type=file]').files[0];
    var data = reader.readAsDataURL(file);
    reset_input();
}

function upload(img){
    data = { image: img }
	$.ajax({
        url: '/model',
        data: data,
        type: 'POST',
        success: function(response) {
            //var prediction = response.digit.replace(/[\[\]']+/g,'')
            alert(response);
        },
        error: function(error) {
            alert('ERROR');
        }
    });/*
    $.post("/model",data,function(resbody){
        alert(resbody);
    })*/
 }
function reset_input(){
    $("#input_file").val("");
}

reader.addEventListener("load", function () {
        $("#img").attr("src",reader.result)
        upload(reader.result)
        console.log("hihi")
    }, false);