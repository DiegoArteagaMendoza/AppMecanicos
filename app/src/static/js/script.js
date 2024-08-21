$('#detailModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Botón que activó el modal
    var client = button.data('client'); // Extrae la información del cliente
    var vehiculo = button.data('vehiculos'); // Extrae la información de los vehículos
    var servicios = button.data('servicio'); // Extrae la información de los servicios
    
    var valorf = 0;
    var name = '';
    var op = '';  
    
    servicios.forEach(servicio => {
        vehiculo.forEach(vehiculo => {
            if (servicio.name === vehiculo.OpcionesTrabajo) {  // Debes comparar con 'servicio.name' no 'servicios.name'
                valorf = servicio.valor;
                name = servicio.name;  // Usa 'servicio.name' para obtener el nombre correcto
                op = vehiculo.OpcionesTrabajo;  // Este está bien como está
            }
        });
    });
    
    console.log(valorf + ' ' + name + ' ' + op);
    

    var modal = $(this);
    modal.find('.modal-body').html(`
        <table class="table table-striped">
            <thead>
                <tr>
                    <th style="color: #fff;">Campo</th>
                    <th style="color: #fff;">Detalle</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="color: #000;">Nombre:</td>
                    <td style="color: #000;">${client.name}</td>
                </tr>
                <tr>
                    <td style="color: #000;">Fecha de ingreso:</td>
                    <td style="color: #000;">${client.date}</td>
                </tr>
                ${(vehiculo && vehiculo.length > 0) ? vehiculo.filter(v => v.idTrabajo === client.idTrabajo).map(vehiculo => `
                    <tr>
                        <td style="color: #000;">Tipo de vehiculo:</td>
                        <td style="color: #000;">${vehiculo.type}</td>
                    </tr>
                    <tr>
                        <td style="color: #000;">Marca, modelo y patente:</td>
                        <td style="color: #000;">${vehiculo.marca + '/' + vehiculo.modelo + '/' + vehiculo.patente}</td>
                    </tr>
                    <tr>
                        <td style="color: #000;">Motivo de entrada:</td>
                        <td style="color: #000;">${vehiculo.OpcionesTrabajo}</td>
                    </tr>
                    <tr>
                        <td style="color: #000;">Descripcion:</td>
                        <td style="color: #000;">${vehiculo.motivo}</td>
                    </tr>
                `).join('') : '<tr><td colspan="2" style="color: #000;">No hay vehículos disponibles.</td></tr>'}
            </tbody>
            <tfoot>
                    <tr>
                        <td style="color: #47bb4c;">Total: $${valorf}</td>
                    </tr>
            </tfoot>
        </table>
    `);
});
