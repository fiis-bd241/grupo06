import React, { useEffect, useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import axios from 'axios';

const ProductionOrderTable = () => {
  const [rows, setRows] = useState([]);

  useEffect(() => {
    axios.get('https://sistema-web-v.onrender.com/sistema/production-orders/')
      .then(response => {
        setRows(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  const columns = [
    { field: 'id_orden_producción', headerName: 'ID Orden Producción', width: 150},
    { field: 'cantidad', headerName: 'Cantidad', width: 100 },
    { field: 'id_lote', headerName: 'ID Lote', width: 110},
    { field: 'cantidad_lote', headerName: 'Cantidad Lote', width: 100 },
    { field: 'tipo_corte', headerName: 'Tipo Corte', width: 110 },
    { field: 'cantidad_cortes', headerName: 'Cantidad Cortes', width: 100},
    { field: 'estado_orden', headerName: 'Estado Orden', width: 100},
    { field: 'progreso_produccion', headerName: 'Progreso Producción (%)', width: 200 },
  ];

  return (
    <div style={{ height: 400, width: '90%' }}>
      <DataGrid rows={rows} columns={columns} pageSize={5} />
    </div>
  );
};

export default ProductionOrderTable;
