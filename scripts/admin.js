$(document).ready ( function(){


   // Reinitialize DataTable
$('#students ').DataTable({
    // DataTable initialization options
});
$('#matrons').DataTable({
    // DataTable initialization options
});


$("#school-bus").DataTable({

});

$("#route-table ,#driver-table").DataTable({

});

//  ADD USERS
$('#add-student-btn').on("click", function(e){
     e.preventDefault();

     $("#add_user_details").modal("show");


     $('#user_detail_form').submit(function (event) {

        event.preventDefault();
        const formAction = $(this).attr('action');

        $.ajax({
            url: formAction,
            type: 'POST',
            data: new FormData(this),
            processData: false,
            contentType: false,
            headers: {
                'X-CSRFToken': getCookie('csrftoken'), // Include CSRF token
            },
            success: function (data) {
                if ('message' in data) {

                    swal({
                        icon: 'success',
                        title: 'Success',
                        text: data.message,
                        buttons: {
                            confirm: {
                                text: 'OK',
                                value: true,
                                visible: true,
                                className: 'sweet-confirm-btn',
                                closeModal: true,
                            },
                        },
                    }).then((value) => {
                        if (value) {
                            setTimeout(function () {
                                location.reload();
                            }, 0);
                        }
                    });

                    $('#user_detail_form')[0].reset();
                    $('#add_user_details').modal('hide');


                } else if ('error' in data) {
                    swal({
                        icon: 'error',
                        title: 'Error',
                        text: data.error,
                    });
                }
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    });


})

// =============== ADD BUSS DETAILS =================#

$('#add-bus-btn').on("click", function(e){
    e.preventDefault();

    $("#add_bus_details").modal("show");


    $('#bus_detail_form').submit(function (event) {

       event.preventDefault();
       const formAction = $(this).attr('action');

       $.ajax({
           url: formAction,
           type: 'POST',
           data: new FormData(this),
           processData: false,
           contentType: false,
           headers: {
               'X-CSRFToken': getCookie('csrftoken'), // Include CSRF token
           },
           success: function (data) {
               if ('message' in data) {

                   swal({
                       icon: 'success',
                       title: 'Success',
                       text: data.message,
                       buttons: {
                           confirm: {
                               text: 'OK',
                               value: true,
                               visible: true,
                               className: 'sweet-confirm-btn',
                               closeModal: true,
                           },
                       },
                   }).then((value) => {
                       if (value) {
                           setTimeout(function () {
                               location.reload();
                           }, 0);
                       }
                   });

                   $('#bus_detail_form')[0].reset();
                   $('#add_bus_details').modal('hide');


               } else if ('error' in data) {
                   swal({
                       icon: 'error',
                       title: 'Error',
                       text: data.error,
                   });
               }
           },
           error: function (error) {
               console.error('Error:', error);
           }
       });
   });


});


/*
    |---------------------------------------------------------
    |             UPDATE DRIVER PROFILE FORM
    |---------------------------------------------------------
    |            
    |
    |
    |
    |
    |------------------------
    */
    $('#driver_profile_form').submit(function (event) {

    event.preventDefault();
    const formAction = $(this).attr('action');

    $.ajax({
        url: formAction,
        type: 'POST',
        data: new FormData(this),
        processData: false,
        contentType: false,
        headers: {
            'X-CSRFToken': getCookie('csrftoken'), // Include CSRF token
        },
        success: function (data) {
            if ('message' in data) {

                swal({
                    icon: 'success',
                    title: 'Success',
                    text: data.message,
                    buttons: {
                        confirm: {
                            text: 'OK',
                            value: true,
                            visible: true,
                            className: 'sweet-confirm-btn',
                            closeModal: true,
                        },
                    },
                }).then((value) => {
                    if (value) {
                        setTimeout(function () {
                            location.reload();
                        }, 0);
                    }
                });

                $('#bus_detail_form')[0].reset();
                $('#add_bus_details').modal('hide');


            } else if ('error' in data) {
                swal({
                    icon: 'error',
                    title: 'Error',
                    text: data.error,
                });
            }
        },
        error: function (error) {
            console.error('Error:', error);
        }
    });
    });


   /*
    |---------------------------------------------------------
    |               DREATE BUSS 
    |---------------------------------------------------------
    |            
    |
    |
    |
    |
    |------------------------
    */
 /*
    |---------------------------------------------------------
    |              SPECIALIST DELETES
    |---------------------------------------------------------
    |            
    |
    |
    |
    |
    |------------------------
    */
    $(document).on('click', '#delete-bus', function (e) {
        e.preventDefault();
    
        const busId = $(this).data('bus-id');
    
        swal({
            title: 'Are you sure?',
            text: `You want to delete this Bus ..!`,
            icon: 'warning',
            buttons: true,
            dangerMode: true,
        }).then((willDelete) => {
            if (willDelete) {
                const url = "/delete_bus/";
                const csrftoken = getCookie('csrftoken');
    
                $.ajax({
                    url: url,
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({ 'busId': busId }),
                    headers: {
                        'X-CSRFToken': csrftoken,
                    },
                    success: function (data) {
                        // Just reload the page without showing any confirmation
                        location.reload();
                    },
                    error: function (error) {
                        swal(`Error deleting Bus is safe!`, {
                            icon: 'error',
                        });
                    }
                });
            } else {
                swal(`Bus is Not Deleted !`);
            }
        });
    });


    /*
    |---------------------------------------------------------
    |              SPECIALIST DELETES
    |---------------------------------------------------------
    |            
    |
    |
    |
    |
    |------------------------
    */
    $(document).on('click', '#delete-driver', function (e) {
        e.preventDefault();
    
        const driverId = $(this).data('driver-id');
    
        swal({
            title: 'Are you sure?',
            text: `You want to delete this Bus Driver..!`,
            icon: 'warning',
            buttons: true,
            dangerMode: true,
        }).then((willDelete) => {
            if (willDelete) {
                const url = "/delete_driver/";
                const csrftoken = getCookie('csrftoken');
    
                $.ajax({
                    url: url,
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({ 'driverId': driverId }),
                    headers: {
                        'X-CSRFToken': csrftoken,
                    },
                    success: function (data) {
                        // Just reload the page without showing any confirmation
                        location.reload();
                    },
                    error: function (error) {
                        swal(`Error deleting Bus driver is safe!`, {
                            icon: 'error',
                        });
                    }
                });
            } else {
                swal(`Bus driver is Not Deleted !`);
            }
        });
    });



     /*
    |---------------------------------------------------------
    |               STUDENT DELETES
    |---------------------------------------------------------
    |            
    |
    |
    |
    |
    |------------------------
    */
    $(document).on('click', '#delete-student', function (e) {
        e.preventDefault();
    
        const studentId = $(this).data('student-id');
    
        swal({
            title: 'Are you sure?',
            text: `You want to delete this Student..!`,
            icon: 'warning',
            buttons: true,
            dangerMode: true,
        }).then((willDelete) => {
            if (willDelete) {
                const url = "/delete_student/";
                const csrftoken = getCookie('csrftoken');
    
                $.ajax({
                    url: url,
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({ 'studentId': studentId }),
                    headers: {
                        'X-CSRFToken': csrftoken,
                    },
                    success: function (data) {
                        // Just reload the page without showing any confirmation
                        location.reload();
                    },
                    error: function (error) {
                        swal(`Error deleting Student is safe!`, {
                            icon: 'error',
                        });
                    }
                });
            } else {
                swal(`Student is Not Deleted !`);
            }
        });
    });



     /*
    |---------------------------------------------------------
    |               DELETE ROUTES
    |---------------------------------------------------------
    |            
    |
    |
    |
    |
    |------------------------
    */
    $(document).on('click', '#delete-route', function (e) {
        e.preventDefault();
    
        const routeId = $(this).data('route-id');
    
        swal({
            title: 'Are you sure?',
            text: `You want to delete this Route`,
            icon: 'warning',
            buttons: true,
            dangerMode: true,
        }).then((willDelete) => {
            if (willDelete) {
                const url = "/delete_route/";
                const csrftoken = getCookie('csrftoken');
    
                $.ajax({
                    url: url,
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({ 'routeId': routeId }),
                    headers: {
                        'X-CSRFToken': csrftoken,
                    },
                    success: function (data) {
                        // Just reload the page without showing any confirmation
                        location.reload();
                    },
                    error: function (error) {
                        swal(`Error deleting Route is safe!`, {
                            icon: 'error',
                        });
                    }
                });
            } else {
                swal(`Route is Not Deleted !`);
            }
        });
    });


    
      /*
    |---------------------------------------------------------
    |               DELETE PATRON
    |---------------------------------------------------------
    |            
    |
    |
    |
    |
    |------------------------
    */
    $(document).on('click', '#delete-patron', function (e) {
        e.preventDefault();
    
        const patronId = $(this).data('patron-id');
    
        swal({
            title: 'Are you sure?',
            text: `You want to Delete`,
            icon: 'warning',
            buttons: true,
            dangerMode: true,
        }).then((willDelete) => {
            if (willDelete) {
                const url = "/delete_patron/";
                const csrftoken = getCookie('csrftoken');
    
                $.ajax({
                    url: url,
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({ 'patronId': patronId }),
                    headers: {
                        'X-CSRFToken': csrftoken,
                    },
                    success: function (data) {
                        // Just reload the page without showing any confirmation
                        location.reload();
                    },
                    error: function (error) {
                        swal(`Error deleting Patron is safe!`, {
                            icon: 'error',
                        });
                    }
                });
            } else {
                swal(`Patron is Not Deleted !`);
            }
        });
    });


   /*
    |---------------------------------------------------------
    |             UPDATE STUDENT PROFILE FORM
    |---------------------------------------------------------
    |            
    |
    |
    |
    |
    |------------------------
    */

    $('#student_profile_form').submit(function (event) {

        event.preventDefault();
        const formAction = $(this).attr('action');
    
        $.ajax({
            url: formAction,
            type: 'POST',
            data: new FormData(this),
            processData: false,
            contentType: false,
            headers: {
                'X-CSRFToken': getCookie('csrftoken'), // Include CSRF token
            },
            success: function (data) {
                if ('message' in data) {
    
                    swal({
                        icon: 'success',
                        title: 'Success',
                        text: data.message,
                        buttons: {
                            confirm: {
                                text: 'OK',
                                value: true,
                                visible: true,
                                className: 'sweet-confirm-btn',
                                closeModal: true,
                            },
                        },
                    }).then((value) => {
                        if (value) {
                            setTimeout(function () {
                                location.reload();
                            }, 0);
                        }
                    });
    
                
                } else if ('error' in data) {
                    swal({
                        icon: 'error',
                        title: 'Error',
                        text: data.error,
                    });
                }
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    });
    

        $('#add-route-btn').on("click", function(e){
            e.preventDefault();
        
            $("#add_route_details").modal("show");
        
        
            $('#route_detail_form').submit(function (event) {
        
               event.preventDefault();
               const formAction = $(this).attr('action');
        
               $.ajax({
                   url: formAction,
                   type: 'POST',
                   data: new FormData(this),
                   processData: false,
                   contentType: false,
                   headers: {
                       'X-CSRFToken': getCookie('csrftoken'), // Include CSRF token
                   },
                   success: function (data) {
                       if ('message' in data) {
        
                           swal({
                               icon: 'success',
                               title: 'Success',
                               text: data.message,
                               buttons: {
                                   confirm: {
                                       text: 'OK',
                                       value: true,
                                       visible: true,
                                       className: 'sweet-confirm-btn',
                                       closeModal: true,
                                   },
                               },
                           }).then((value) => {
                               if (value) {
                                   setTimeout(function () {
                                       location.reload();
                                   }, 0);
                               }
                           });
        
                           $('#route_detail_form')[0].reset();
                           $('#add_route_details').modal('hide');
        
        
                       } else if ('error' in data) {
                           swal({
                               icon: 'error',
                               title: 'Error',
                               text: data.error,
                           });
                       }
                   },
                   error: function (error) {
                       console.error('Error:', error);
                   }
               });
           });
        
        
        });



      /*
    |---------------------------------------------------------
    |             UPDATE DRIVER PROFILE FORM
    |---------------------------------------------------------
    |            
    |
    |
    |
    |
    |------------------------
    */

    $('#patron_profile_form').submit(function (event) {

        event.preventDefault();
        const formAction = $(this).attr('action');
    
        $.ajax({
            url: formAction,
            type: 'POST',
            data: new FormData(this),
            processData: false,
            contentType: false,
            headers: {
                'X-CSRFToken': getCookie('csrftoken'), // Include CSRF token
            },
            success: function (data) {
                if ('message' in data) {
    
                    swal({
                        icon: 'success',
                        title: 'Success',
                        text: data.message,
                        buttons: {
                            confirm: {
                                text: 'OK',
                                value: true,
                                visible: true,
                                className: 'sweet-confirm-btn',
                                closeModal: true,
                            },
                        },
                    }).then((value) => {
                        if (value) {
                            setTimeout(function () {
                                location.reload();
                            }, 0);
                        }
                    });
    
                
                } else if ('error' in data) {
                    swal({
                        icon: 'error',
                        title: 'Error',
                        text: data.error,
                    });
                }
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    });
    



    /*
    |---------------------------------------------------------
    |              FETCH GROUPS 
    |---------------------------------------------------------
    |            
    |
    |
    |
    |
    |------------------------
    */
    $(document).ready(function () {

        const csrftoken = $('[name=csrfmiddlewaretoken]').val();
        // Fetch initial group when the page loads
        $.ajax({
            url: '/fetch_buss/',
            type: 'GET',
            dataType: 'json',
            success: function (response) {

                $('#buss').html(response.options);


            }


        });

    });

    
/*
    |---------------------------------------------------------
    |              FETCH GROUPS 
    |---------------------------------------------------------
    |            
    |
    |
    |
    |
    |------------------------
    */
    $(document).ready(function () {

        const csrftoken = $('[name=csrfmiddlewaretoken]').val();
        // Fetch initial group when the page loads
        $.ajax({
            url: '/fetch_groups/',
            type: 'GET',
            dataType: 'json',
            success: function (response) {

                $('#group').html(response.options);


            }


        });

    });


    /*
    |---------------------------------------------------------
    |              FETCH GROUPS 
    |---------------------------------------------------------
    |            
    |
    |
    |
    |
    |------------------------
    */
    $(document).ready(function () {

        const csrftoken = $('[name=csrfmiddlewaretoken]').val();
        // Fetch initial group when the page loads
        $.ajax({
            url: '/fetch_drivers/',
            type: 'GET',
            dataType: 'json',
            success: function (response) {

                $('#drivers').html(response.options);


            }


        });

    });








    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }



});

