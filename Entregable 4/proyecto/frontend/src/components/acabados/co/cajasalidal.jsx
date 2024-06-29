import React, { useEffect, useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import axios from 'axios';

const columns = [
  { field: 'id_caja', headerName: 'ID Caja', width: 150 },
  { field: 'id_salida', headerName: 'ID Salida', width: 150 },
  { field: 'fecha_salida', headerName: 'Fecha de Salida', width: 200 },
];

const CajaSalidaTable = () => {
  const [rows, setRows] = useState([]);

  useEffect(() => {
    axios.get('https://sistema-web-v.onrender.com/sistema/caja_salida/')
      .then(response => {
        const dataWithIds = response.data.map((row, index) => ({
          id: index,
          ...row
        }));
        setRows(dataWithIds);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div style={{ height: 300, width: '50%' }}>
      <DataGrid rows={rows} columns={columns} pageSize={5}  density="compact"/>
    </div>
  );
};

export default CajaSalidaTable;
