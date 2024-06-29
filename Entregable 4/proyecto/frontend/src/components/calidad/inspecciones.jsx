
import React, { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { Select, MenuItem, FormControl, InputLabel } from '@mui/material';

const CalidadInspecc = () => {
  const [inspecciones, setInspecciones] = useState([]);
  const [ordenesProduccion, setOrdenesProduccion] = useState([]);
  const [selectedOrden, setSelectedOrden] = useState('');

  useEffect(() => {
    fetch('https://sistema-web-v.onrender.com/sistema/inspeccionescal/')
      .then(response => response.json())
      .then(data => setInspecciones(data));

    fetch('https://sistema-web-v.onrender.com/sistema/ordenes-produccioncal/')
      .then(response => response.json())
      .then(data => setOrdenesProduccion(data));
  }, []);

  const handleOrdenChange = (event) => {
    const selectedValue = event.target.value;
    setSelectedOrden(selectedValue);

    fetch(`https://sistema-web-v.onrender.com/sistema/inspeccionescal/?orden=${selectedValue}`)
      .then(response => response.json())
      .then(data => setInspecciones(data));
  };

  const columns = [
    { field: 'ID_ORDEN_PRODUCCIÓN', headerName: 'ID Orden Producción', width: 80 },
    { field: 'ID_INSPECCION', headerName: 'ID Inspección', width: 80 },
    { field: 'ID_LOTE', headerName: 'ID Lote', width: 80 },
    { field: 'FECHA_INSPECCION', headerName: 'Fecha Inspección', width: 80 },
    { field: 'ID_AQL_LOTE_RANGO', headerName: 'ID AQL Lote Rango', width: 80},
    { field: 'CANTIDAD_DEFECTUOSOS', headerName: 'Cantidad Defectuosos', width: 80 },
    { field: 'ID_AQL_CODIGO', headerName: 'ID AQL Código', width: 80 },
    { field: 'ID_AQL_NIVEL', headerName: 'ID AQL Nivel', width:80 },
    { field: 'ID_AQL_SIGNIFICANCIA', headerName: 'ID AQL Significancia', width: 80 },
    { field: 'ID_ESTADO', headerName: 'ID Estado', width: 80 },
    { field: 'ID_RESULTADO', headerName: 'ID Resultado', width: 80 },
  ];

  return (
    <div style={{ height: 400, width: '100%' }}>
      <FormControl variant="outlined" style={{ marginBottom: '20px' }}>
        <InputLabel id="orden-select-label">Orden Producción</InputLabel>
        <Select
          labelId="orden-select-label"
          id="orden-select"
          value={selectedOrden}
          onChange={handleOrdenChange}
          label="Orden Producción"
        >
          {ordenesProduccion.map((orden) => (
            <MenuItem key={orden.ID_ORDEN_PRODUCCIÓN} value={orden.ID_ORDEN_PRODUCCIÓN}>
              {orden.ID_ORDEN_PRODUCCIÓN}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
      <DataGrid rows={inspecciones} columns={columns} pageSize={5} />
    </div>
  );
};

export default CalidadInspecc;





