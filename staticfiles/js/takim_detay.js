$("#proje-yonet").on('click', function () {
    let proje_slug = $(this).attr('data-slug');
    //toDo: modal açılınca proje detaylarını ajax ile getir ve formu doldur
    let form_data = new FormData(); // FormData instance oluşturduk
    form_data.append('proje_slug', proje_slug); // form data'ya  değer ekledik (key-value)
    form_data.append('islem_tipi', 'proje_detay_getir');
    let url = $("#ajax-url").val();
    $.ajax({
        url: url, // url'e istek atıyoruz
        type: "post", // post request
        data: form_data, // veri olarak form_data değişkenini yolluyoruz
        contentType: false,
        processData: false,
        success: function (data) {
            $('#duzenle_ad').val(data.proje_adi);
            $('#duzenle_aciklama').val(data.proje_aciklama);
            $('#duzenle_baslangic_tarih').val(data.baslangic_tarihi);
            $('#duzenle_bitis_tarih').val(data.bitis_tarihi);
        }
    });
});