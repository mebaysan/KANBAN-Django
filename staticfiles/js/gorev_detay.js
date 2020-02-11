$(".custom-control-label").on('click', (e) => {
    //toDo: görev işlem durum ajaxz ile değiştir
    console.log($(this).attr('data-pk'));
    // $.ajax({
    //     url: url,
    //     type: "post",
    //     data: form_data,
    //     contentType: false,
    //     processData: false,
    //     success: function (data) {
    //         return true;
    //     }
    // });
});