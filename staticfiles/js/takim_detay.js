$("#proje-yonet").on('click', function(){
    let proje_slug = $(this).attr('data-slug');
    //toDo: modal açılınca proje detaylarını ajax ile getir ve formu doldur
    let form_data = new FormData(); // FormData instance oluşturduk
    form_data.append('proje_slug', proje_slug); // form data'ya  değer ekledik (key-value)
    form_data.append('islem_tipi', 'proje_detay_getir');
    let url = $("#ajax-url").val();
    console.log(url);
    $.ajax({
        url: url, // url'e istek atıyoruz
        type: "post", // post request
        data: form_data, // veri olarak form_data değişkenini yolluyoruz
        contentType: false,
        processData: false,
        success: function (data) {
            return true;
        }
    });
});