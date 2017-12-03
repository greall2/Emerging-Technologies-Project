var reader  = new FileReader();

//declaring the files that are allowedyo be uploaded 
var files_allwd = ['gif','png','jpg','jpeg'];


function upload_file(){
    // Adapted from: https://stackoverflow.com/questions/651700/how-to-have-jquery-restrict-file-types-on-upload
    
    var file_name = $('#input_file');
    var extension = file_name.val().split('.').pop().toLowerCase();
    if ($(file_name).get(0).files.length === 0) {
        alert("No files selected.");
        return;
    }else if($.inArray(extension, files_allwd) == -1) {
        alert('ERROR! File must be one of the following:  .jpg, .png , .gif');
        return;
    }
    //adaptd from https://developer.mozilla.org/en-US/docs/Web/API/FileReader/readAsDataURL
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
           alert(response);
        },
        error: function(error) {
            alert('ERROR');
        }
    });

 }
function reset_input(){
    $("#input_file").val("");
}
//uploading and loading image into the image holder 
reader.addEventListener("load", function () {
        $("#img").attr("src",reader.result)
        upload(reader.result)
        console.log("hihi")
    }, false);