import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { DataGrid } from '@mui/x-data-grid';
import axios from 'axios';

const CajaPrendaList = () => {
  const [cajas, setCajas] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    axios.get('https://sistema-web-v.onrender.com/sistema/cajas')
      .then(response => {
        // Add an id field to each row by mapping id_caja to id
        const dataWithId = response.data.map((row) => ({
          ...row,
          id: row.id_caja,
        }));
        setCajas(dataWithId);
      })
      .catch(error => console.error(error));
  }, []);

  const columns = [
    { field: 'id_caja', headerName: 'ID Caja', width: 150 },
    { field: 'tipo_prenda', headerName: 'Tipo Prenda', width: 150 },
    { field: 'cantidad', headerName: 'Cantidad', width: 150 },
    { field: 'fecha_creacion', headerName: 'Fecha Creación', width: 200 },
    { field: 'estado', headerName: 'Estado', width: 150 },
  ];

  const handleRowClick = (params) => {
    navigate(`/cajas/${params.row.id_caja}`);
  };

  return (
    <div style={{ height: 300, width: '80%' }}>
      <DataGrid
        rows={cajas}
        columns={columns}
        pageSize={5}
        onRowClick={handleRowClick}
        density="compact"
      />
    </div>
  );
};

export default CajaPrendaList;
