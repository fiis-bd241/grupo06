import React from 'react';
import { Box, Typography, Link } from '@mui/material';
//import "../estilos/home.css"; // Si aún necesitas tu CSS personalizado

const Garea = () => {
  return (
    <Box className="nos-container" sx={{ padding: 8, backgroundColor: '#f0f0f0', borderRadius: 2, boxShadow: 3, maxWidth: '95%', margin: '0 auto' }}>
  <Typography variant="h4" component="h2" gutterBottom sx={{ fontSize: '1.5rem', fontWeight: 'bold', marginBottom: '1rem' }}>
    Datos generales
  </Typography>
  <Box component="section" mb={2}>
    <Typography variant="h5" component="h3" sx={{ fontSize: '1rem', fontWeight: 'bold', marginBottom: '0.5rem' }}>
      Title-1
    </Typography>
    <Typography variant="body1" color="textSecondary" sx={{ fontSize: '1rem', marginBottom: '0.5rem' }}>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. in voluptate velit esse cillum dolore
    </Typography>
  </Box>
  <Box component="section">
    <Link href="https://www.vircatex.com/" target="_blank" rel="noopener noreferrer" color="primary" underline="hover">
      Visita nuestro sitio web.
    </Link>
  </Box>
</Box>
  );
}

export default Garea;
