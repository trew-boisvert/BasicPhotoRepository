"use strict";

$("#logout").on('click', (evt) => {
    $('#logout').hide();
    $('#delete-account').hide();
    $.post('handle-logout', (res) => {
        $('#logout-text').html(res['message'])
    })
})

$("#display-post-list").on('click', (evt) => {
    $('#display-post-list').hide();
    $.post('/api/posts', (res) => {
        for(const key in res){
            $('#current-posts').append(`<div> <h3>${res[key]}</h3> <a href="/delete/${key}" class="btn btn-default"><i class="far fa-trash-alt"></i></a></div>`)
        }
    })
})

//this deletes posts.  not to be confused with deleting a user profile.
$("#goodbye-forever").on('click', (evt) => {
    $.post('/api/delete', (res) => {
        $('#goodbye-forever').hide();
        $('#say-goodbye').append(`<p>${res['message']}</p>`);
        $('#say-goodbye').append(`<a href="http://0.0.0.0:5000/profile" class="btn btn-default">Return to Profile</a>`);
    })
})

//this deletes a user profile, and their attendant posts.
$("#delete-account").on('click', (evt) => {
    $.post('/api/accountdelete', (res) => {
        $('#delete-account').hide();
        $('#logout').hide();
        $('#delete-account-text').append(`<p>${res['message']}</p>`);
    })
})

async function imageUpload(files) {
    const url = "https://api.cloudinary.com/v1_1/knittr/image/upload";
    const uploadData = new FormData(); 

    let file = files[0];
    uploadData.append("file", file);
    uploadData.append("upload_preset", "r8rsqkah");

    let response = await fetch(url, {
        method: "POST",
        body: uploadData
    });

    let json = await response.json();

    return json.url
}

$('#upload-photos').on('submit', (evt) => {
    evt.preventDefault();

    const media_files = $('#photo_upload').prop('files');
    const cloud_url = imageUpload(media_files);

    cloud_url.then((res_url) => {
        
        const photo_post_data = {
            'post_name': $('#post-name').val(),
            'post_comment': $('#post-comment').val(),
            'img_url': res_url
        }
        console.log(photo_post_data)
        $.post('/api/photos', photo_post_data, (res) => {
            if (res.status === 'ok') {
                $('#photo_upload_success').html(`Your post has been added to the database.`)
            } 
        });  
    });
});