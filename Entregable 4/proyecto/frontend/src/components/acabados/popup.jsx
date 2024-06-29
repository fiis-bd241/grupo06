// Popup.jsx
import React from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import { styled } from '@mui/material/styles';

// Typography con estilo específico
const CustomTypography = styled(Typography)(({ theme }) => ({
    fontSize: '18px',
    fontWeight: 'bold',
    
  }));

function AsignarCajaSalida({ open, onClose }) {
  const handleClose = () => {
    onClose(); // Llama a la función para cerrar el popup desde el padre
  };

  if (!open) return null; // No renderizar si no está abierto

  return (
    <div className="overlay">
    <Box
      display="flex"
      flexDirection="column"
      alignItems="center"
      justifyContent="center"
      mt={4}
      p={2}
      style={{ position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', backgroundColor: 'white', zIndex: 999, boxShadow: '0px 0px 10px rgba(0, 0, 0, 0.1)', width: 400 }}
    >
      <CustomTypography variant="h4" gutterBottom>
        Asignar Caja Salida
      </CustomTypography>
      <Box width="100%">
        <TextField
          label="Caja salida"
          variant="outlined"
          size="small"
          margin="normal"
          fullWidth
        />
      </Box>
      <Box mt={2} width="100%">
        <Button variant="contained" color="primary" fullWidth style={{ marginBottom: '8px' }}>
          Actualizar
        </Button>
        <Button variant="contained" color="secondary" fullWidth onClick={handleClose}>
          Cancelar
        </Button>
      </Box>
    </Box>
    </div>
  );
}

export default AsignarCajaSalida;