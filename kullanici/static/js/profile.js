$('#sifre_guncelle_btn').click((e) => {
    e.preventDefault(); // formu submit eden eventi keser
    let eski_sifre = $('#eski_sifre').val();
    let yeni_sifre = $('#yeni_sifre').val();
    let yeni_sifre_kontrol = $('#yeni_sifre_kontrol').val();
    if (yeni_sifre_kontrol !== yeni_sifre) {
        new Toast({
            message: 'Şifreler eşleşmiyor!',
            type: 'danger'
        });
    } else if (!yeni_sifre_kontrol || !yeni_sifre || !eski_sifre) {
        new Toast({
            message: 'Şifre alanları boş bırakılamaz!',
            type: 'danger'
        });
    } else {
        $('#sifre_guncelle_form').submit(); // formu submit eder

    }
});
//toDo: Eski şifre kontrolü yap!