

// https://sistema-web-v.onrender.com/sistema/get_filtered_data/
// DataTable.js
import React, { useState, useEffect, useCallback } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import axios from 'axios';
import FilterDropdown from './dropdownconsul';


const DataTable = () => {
  const [data, setData] = useState([]);
  const [e2Nombre, setE2Nombre] = useState('');
  const [tmpNombre, setTmpNombre] = useState('');

  const fetchData = useCallback(async () => {
    try {
      const response = await axios.get('https://sistema-web-v.onrender.com/sistema/get_filtered_data/', {
        params: {
          e2_nombre: e2Nombre,
          tmp_nombre: tmpNombre,
        },
      });
      setData(response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }, [e2Nombre, tmpNombre]);

  useEffect(() => {
    fetchData();
  }, [fetchData]); // useCallback ensures fetchData reference remains stable

  const columns = [
    { field: 'id_lote', headerName: 'ID Lote', width: 150 },
    { field: 'denominacion_social', headerName: 'Proveedor', width: 200 },
    { field: 'id_espacio', headerName: 'ID Espacio', width: 150 },
    { field: 'fecha_entrada', headerName: 'Fecha Entrada', width: 200 },
    { field: 'tipo_materia_prima', headerName: 'Tipo Materia Prima', width: 200 },
  ];

  return (
    <div>
      <div style={{ display: 'flex', marginBottom: '20px' }}>
        <FilterDropdown
          label="Estado"
          options={['Disponible', 'No Disponible']}
          value={e2Nombre}
          onChange={(e) => setE2Nombre(e.target.value)}
        />
        <FilterDropdown
          label="Tipo Materia Prima"
          options={['Jersey', 'Otro']}
          value={tmpNombre}
          onChange={(e) => setTmpNombre(e.target.value)}
        />
      </div>
      <div style={{ height: 400, width: '100%' }}>
        <DataGrid rows={data} columns={columns} pageSize={5} />
      </div>
    </div>
  );
};

export default DataTable;
