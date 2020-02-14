$("#duzenle_baslangic_tarih").flatpickr(); // bunları js kütüphanesi olarak kullanabilmemiz için init etmemiz gerekiyor
$("#duzenle_bitis_tarih").flatpickr();
$("#proje-yonet").on('click', function () {
    let proje_slug = $(this).attr('data-slug');
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
            $("#proje_guncelle_slug").val(data.proje_slug);
            $('#duzenle_ad').val(data.proje_adi);
            $('#duzenle_aciklama').val(data.proje_aciklama);
            $('#duzenle_baslangic_tarih').val(data.baslangic_tarihi);
            $('#duzenle_bitis_tarih').val(data.bitis_tarihi);

        }
    });
});

$("#proje-guncelle-button").on('click', function (e) {
    e.preventDefault();
    let form_data = new FormData(); // FormData instance oluşturduk
    form_data.append('proje_slug', $("#proje_guncelle_slug").val()); // form data'ya  değer ekledik (key-value)
    form_data.append('islem_tipi', 'proje_guncelle');
    form_data.append('proje_ad', $("#duzenle_ad").val());
    form_data.append('proje_aciklama', $("#duzenle_aciklama").val());
    form_data.append('proje_baslangic', $("#duzenle_baslangic_tarih").val());
    form_data.append('proje_bitis', $("#duzenle_bitis_tarih").val());
    let url = $("#ajax-url").val();
    $.ajax({
        url: url,
        type: "post",
        data: form_data,
        contentType: false,
        processData: false,
        success: function (data) {
            if (data.success === true) {
                location.reload();

            }
        }
    });
});