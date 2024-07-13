$("form[name=signup_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  //toma todos los campos del objeto
  var data = $form.serialize();

  $.ajax({
    url: "/usuario/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      console.log(resp);
      window.location.href = "/home/";
    },
    error: function(resp) {
      console.log(resp);
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});



$("form[name=login_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/usuario/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/home/";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});


//################################################

$("form[name=add_trainer_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/entrenador/add_trainer",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/entrenador/";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});



$(document).on("click", ".btn-danger", function(e) {
  e.preventDefault();
  var url = $(this).attr("href");
  
  $.ajax({
      url: url,
      type: "GET",
      success: function(resp) {
          window.location.href = "/entrenador/"; // Redirige después de eliminar
      },
      error: function(resp) {
          alert("Error al eliminar el entrenador: " + resp.responseJSON.error);
      }
  });
});



$("form[action*='edit_trainer']").submit(function(e) {
  e.preventDefault();
  var $form = $(this);
  var url = $form.attr('action');
  var data = $form.serialize();

  $.ajax({
      url: url,
      type: "POST",
      data: data,
      success: function(resp) {
          window.location.href = "/entrenador/"; // Redirige después de editar
      },
      error: function(resp) {
          alert("Error al editar el entrenador: " + resp.responseJSON.error);
      }
  });
});