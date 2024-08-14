$('#detailModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Botón que activó el modal
    var client = button.data('client'); // Extrae la información del cliente
    var vehiculo = button.data('vehiculos'); // Extrae la información de los vehículos

    // Verifica que los datos del cliente no sean undefined
    console.log(client);
    console.log(vehiculo);

    var modal = $(this);
    modal.find('.modal-body').html(`
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Campo</th>
                    <th>Detalle</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Nombre:</strong></td>
                    <td>${client.name}</td>
                </tr>
                <tr>
                    <td><strong>Teléfono:</strong></td>
                    <td>${client.phone}</td>
                </tr>
                <tr>
                    <td><strong>Correo:</strong></td>
                    <td>${client.email}</td>
                </tr>
                <tr>
                    <td><strong>Fecha:</strong></td>
                    <td>${client.date}</td>
                </tr>
                ${(vehiculo && vehiculo.length > 0) ? vehiculo.filter(v => v.id === client.id).map(vehiculo => `
                    <tr>
                        <td><strong>Tipo de vehiculo:</strong></td>
                        <td>${vehiculo.type}</td>
                    </tr>
                    <tr>
                        <td><strong>Marca:</strong></td>
                        <td>${vehiculo.marca}</td>
                    </tr>
                    <tr>
                        <td><strong>Modelo:</strong></td>
                        <td>${vehiculo.modelo}</td>
                    </tr>
                    <tr>
                        <td><strong>Trabajo:</strong></td>
                        <td>${vehiculo.OpcionesTrabajo}</td>
                    </tr>
                    <tr>
                        <td><strong>Motivo:</strong></td>
                        <td>${vehiculo.motivo}</td>
                    </tr>
                `).join('') : '<tr><td colspan="2">No hay vehículos disponibles.</td></tr>'}
            </tbody>
        </table>
    `);
    // modal.find('.modal-body').html(`
    //     <p><strong>Nombre:</strong><br> ${client.name}</p>
    //     <p><strong>Teléfono:</strong><br> ${client.phone}</p>
    //     <p><strong>Correo:</strong><br> ${client.email}</p>
    //     <p><strong>Fecha:</strong><br> ${client.date}</p>
        
    //     ${(vehiculo && vehiculo.length > 0) ? vehiculo.map(vehiculo => `
    //         <p><strong>Tipo de vehiculo:</strong><br> ${vehiculo.type}</p>
    //         <p><strong>Marca:</strong><br> ${vehiculo.marca}</p>
    //         <p><strong>Modelo:</strong><br> ${vehiculo.modelo}</p>
    //         <p><strong>Motivo:</strong><br> ${vehiculo.motivo}</p>
    //     `).join('') : '<p>No hay vehículos disponibles.</p>'}
    // `);
});
