import React, { useEffect, useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import axios from 'axios';

const columns = [
  { field: 'fecha_actividad', headerName: 'Fecha Actividad', width: 150 },
  { field: 'id_orden_producción', headerName: 'ID Orden Producción', width: 150 },
  { field: 'cantidad_orden', headerName: 'Cantidad Orden', width: 150 },
  { field: 'id_maquina', headerName: 'ID Maquina', width: 150 },
  { field: 'cantidad_realizar', headerName: 'Cantidad Realizar', width: 150 },
  { field: 'tipo_corte', headerName: 'Tipo Corte', width: 150 },
];

function ActividadDiariaTable() {
  const [rows, setRows] = useState([]);

  useEffect(() => {
    axios.get('https://sistema-web-v.onrender.com/sistema/actividad-diaria/')
      .then(response => {
        setRows(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGrid 
        rows={rows} 
        columns={columns} 
        pageSize={5} 
        getRowId={(row) => `${row.fecha_actividad}-${row.id_orden_producción}-${row.id_maquina}`}
      />
    </div>
  );
}

export default ActividadDiariaTable;
