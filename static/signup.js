$(document).ready(function () {
  $('#signup-form').submit(function (event) {
    event.preventDefault();

    var formData = $(this).serialize();
    $.ajax({
      url: '/api/users/signup',
      type: 'POST',
      data: formData,
      success: function (response) {
        console.log(response);
        alert('회원가입 성공');
        window.location.href = '/';
      },
      error: function () {
        alert('오류 발생');
      },
    });
  });
});
