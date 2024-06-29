import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { DataGrid } from '@mui/x-data-grid';
import { TextField, MenuItem, Button } from '@mui/material';


const Lotesentrealmacen = () => {
        const [rows, setRows] = useState([]);
        const [filters, setFilters] = useState({
          nombre_material: '',
          nombre_proveedor: '',
          fecha_entrada: '',
        });
      
        const fetchData = async () => {
          const response = await axios.get('https://sistema-web-v.onrender.com/sistema/lote_entradalist/', {
            params: filters,
          });
          setRows(response.data);
        };
      
        useEffect(() => {
          fetchData();
        }, [filters]);
      
        const handleFilterChange = (e) => {
          setFilters({
            ...filters,
            [e.target.name]: e.target.value,
          });
        };
      
        const columns = [
          { field: 'fecha_entrada', headerName: 'Fecha Entrada', width: 150 },
          { field: 'id_lote', headerName: 'ID Lote', width: 100 },
          { field: 'nombre_material', headerName: 'Material', width: 150 },
          { field: 'nombre_proveedor', headerName: 'Proveedor', width: 200 },
          { field: 'cantidad', headerName: 'Cantidad', width: 100 },
        ];
      
        return (
          <div style={{ height: 400, width: '100%' }}>
            <div>
              <TextField
                label="Materia Prima"
                name="nombre_material"
                value={filters.nombre_material}
                onChange={handleFilterChange}
                select
              >
                <MenuItem value="">Seleccione</MenuItem>
                {/* Add other material options here */}
              </TextField>
              <TextField
                label="Proveedor"
                name="nombre_proveedor"
                value={filters.nombre_proveedor}
                onChange={handleFilterChange}
                select
              >
                <MenuItem value="">Seleccione</MenuItem>
                {/* Add other provider options here */}
              </TextField>
              <TextField
                label="Fecha"
                name="fecha_entrada"
                type="date"
                value={filters.fecha_entrada}
                onChange={handleFilterChange}
                InputLabelProps={{
                  shrink: true,
                }}
              />
              <Button variant="contained" onClick={fetchData}>Buscar</Button>
            </div>
            <DataGrid rows={rows} columns={columns} pageSize={5} getRowId={(row) => row.id_lote} />
          </div>
        );
      };
      
      export default Lotesentrealmacen;
      