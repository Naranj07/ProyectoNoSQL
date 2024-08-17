
//############### Login Usuario ####################
$("form[name=signup_form").submit(function(e) {
  e.preventDefault(); // Evitar la acción predeterminada del formulario

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serializeArray(); // Serializar el formulario
/*  var dataFactura= $form.serializeArray(); 

  // Capturar valores específicos para la factura
  var nombreCompleto = $form.find("input[name='Nombre_completo']").val();
  var membresia = $form.find("select[name='Membresia_id'] option:selected").text();
  var precio = $form.find("select[name='Membresia_id'] option:selected").data("precio");
  var fecha = $("#fecha").val();
  var metodoPago = $("#metodo_pago").val();

  var facturaData = {
    usuario: nombreCompleto,
    detalle_factura: membresia,
    pago: precio,
    fecha: fecha,
    metodo_de_pago: metodoPago
  };*/

  // Primera petición AJAX para crear el usuario
  $.ajax({
    url: "/usuario/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      console.log(resp);

      // Segunda petición AJAX para crear la factura
      $.ajax({
        url: "/factura/add_factura",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
          console.log("Factura creada:", resp);
          window.location.href = "/home/"; // Redirige a home después de la creación exitosa
        },
        error: function(resp) {
          console.log("Error al crear factura:", resp);
        }
      });
    },
    error: function(resp) {
      console.log(resp);
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });
});



/*$("form[name=signup_form").submit(function(e) {

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
});*/



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
//para la facturación vista en registro
$(document).ready(function() {
  $("#facturar-btn").click(function() {
    var $select = $("#Membresia_id");
    var tipo = $select.find("option:selected").data("tipo");
    var precio = $select.find("option:selected").data("precio");

    $("#mem").text(tipo);
    $("#pago").text(precio);
    $("#hiddenMem").val(tipo);
    $("#hiddenPago").val(precio);
  });
});


//#################### Entrenador ######################

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



$(document).on("click", ".btn-danger-trainer", function(e) {
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



//###################### Ejercicio #####################


$("form[name=add_exercise_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/ejercicio/add_exercise",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/ejercicio/";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});



$(document).on("click", ".btn-danger-exercise", function(e) {
  e.preventDefault();
  var url = $(this).attr("href");
  
  $.ajax({
      url: url,
      type: "GET",
      success: function(resp) {
          window.location.href = "/ejercicio/"; // Redirige después de eliminar
      },
      error: function(resp) {
          alert("Error al eliminar el ejercicio: " + resp.responseJSON.error);
      }
  });
});



$("form[action*='edit_exercise']").submit(function(e) {
  e.preventDefault();
  var $form = $(this);
  var url = $form.attr('action');
  var data = $form.serialize();

  $.ajax({
      url: url,
      type: "POST",
      data: data,
      success: function(resp) {
          window.location.href = "/ejercicio/"; // Redirige después de editar
      },
      error: function(resp) {
          alert("Error al editar el ejercicio: " + resp.responseJSON.error);
      }
  });
});