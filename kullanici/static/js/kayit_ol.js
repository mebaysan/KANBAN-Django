$('#kayit_btn').click((e) => {
    e.preventDefault(); // formu submit eden eventi keser
    let password = $('#password').val();
    let password_check = $('#password_check').val();
    if (password !== password_check) {
        new Toast({
            message: 'Şifreler eşleşmiyor!',
            type: 'danger'
        });
    } else {
        $('#kayit_ol_form').submit(); // formu submit eder

    }
});