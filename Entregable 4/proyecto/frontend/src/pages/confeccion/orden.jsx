import React, { useState, useEffect, useCallback } from 'react';
import axios from 'axios';
import Sidenav from '../../components/Sidenav';
import Navbar from '../../components/Navbar';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import MenuItem from '@mui/material/MenuItem';
import SkeletonLoader from '../SkeletonLoader';
import CajaPrendaList from '../../components/acabados/cajalista';

export default function OrdenConfeccionPage() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState({
    estado: '',
    fecha_inicio: '',
    fecha_fin: '',
  });

  // Definir fetchData utilizando useCallback
  const fetchData = useCallback(async () => {
    setLoading(true);
    try {
      const response = await axios.get('/api/ord_prod_conf_view/', {
        params: {
          estado: filters.estado,
          fecha_inicio: filters.fecha_inicio,
          fecha_fin: filters.fecha_fin,
        },
      });
      setData(response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setLoading(false);
    }
  }, [filters]);

  // UseEffect para llamar a fetchData cuando cambian los filtros
  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const handleFilterChange = (e) => {
    const { name, value } = e.target;
    setFilters((prevFilters) => ({
      ...prevFilters,
      [name]: value,
    }));
  };

  const clearFilters = () => {
    setFilters({
      estado: '',
      fecha_inicio: '',
      fecha_fin: '',
    });
  };

  const handleClick = () => {
    // Función para manejar el clic en el botón de Reporte
    console.log('Handle Reporte');
    // Implementa la lógica necesaria para el reporte
  };

  return (
    <>
      <Navbar />
      <Box height={30} />
      <Box sx={{ display: 'flex' }}>
        <Sidenav />

        <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
          <h1>Área de Confección</h1>
          <Typography paragraph>resumen</Typography>
          <h3>Orden de producción</h3>

          {/* Filtros */}
          <Box sx={{ mb: 2 }}>
            <TextField
              select
              name="estado"
              label="Estado"
              variant="outlined"
              value={filters.estado}
              onChange={handleFilterChange}
              sx={{ mr: 2 }}
              fullWidth
            >
              <MenuItem value="">Seleccionar Estado</MenuItem>
              <MenuItem value="No iniciado">No iniciado</MenuItem>
              <MenuItem value="En proceso">En proceso</MenuItem>
              <MenuItem value="Atrasado">Atrasado</MenuItem>
            </TextField>
            <TextField
              name="fecha_inicio"
              label="Fecha de Inicio"
              variant="outlined"
              type="date"
              value={filters.fecha_inicio}
              onChange={handleFilterChange}
              sx={{ mr: 2 }}
              InputLabelProps={{
                shrink: true,
              }}
            />
            <TextField
              name="fecha_fin"
              label="Fecha de Fin"
              variant="outlined"
              type="date"
              value={filters.fecha_fin}
              onChange={handleFilterChange}
              sx={{ mr: 2 }}
              InputLabelProps={{
                shrink: true,
              }}
            />
            <Button
              variant="contained"
              color="primary"
              onClick={fetchData}
              sx={{ mr: 2 }}
            >
              Aplicar Filtros
            </Button>
            <Button variant="outlined" color="secondary" onClick={clearFilters}>
              Limpiar Filtros
            </Button>
          </Box>

          {/* Contenido principal */}
          {loading ? (
            <SkeletonLoader />
          ) : (
            <>
              {/* Aquí va tu tabla de datos */}
              <table>
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Estado</th>
                    <th>Fecha de Inicio</th>
                    <th>Fecha de Fin</th>
                    {/* Añadir más columnas según tus datos */}
                  </tr>
                </thead>
                <tbody>
                  {data.map((item) => (
                    <tr key={item.id}>
                      <td>{item.id}</td>
                      <td>{item.estado}</td>
                      <td>{item.fecha_inicio}</td>
                      <td>{item.fecha_fin}</td>
                      {/* Añadir más celdas según tus datos */}
                    </tr>
                  ))}
                </tbody>
              </table>

              <div>
                <CajaPrendaList />
              </div>

              <div>
                <Box display="flex" justifyContent="flex-end" mt={2}>
                  <Button
                    variant="contained"
                    color="primary"
                    onClick={handleClick}
                  >
                    Reporte
                  </Button>
                </Box>
              </div>
            </>
          )}
        </Box>
      </Box>
    </>
  );
}
