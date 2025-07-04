$(document).ready(function () {
  $('#login-form').submit(function (event) {
    event.preventDefault();

    var loginData = {
      email: $('input[name="login-email"]').val(),
      password: $('input[name="login-password"]').val(),
    };

    $.ajax({
      url: '/api/users/login',
      type: 'POST',
      data: loginData,
      success: function (response) {
        alert('로그인 성공');
        alert(response.name);
        window.location.href = '/main';
      },
      error: function () {
        alert('오류 발생');
      },
    });
  });
});
