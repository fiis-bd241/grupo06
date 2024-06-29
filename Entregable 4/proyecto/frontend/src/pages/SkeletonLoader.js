// SkeletonLoader.js
import React from 'react';
import Skeleton from '@mui/material/Skeleton';
import Box from '@mui/material/Box';

const SkeletonLoader = () => {
  return (
    <Box sx={{ p: 3 }}>
      <Skeleton variant="text" width="30%" />
      <Skeleton variant="rectangular" width="100%" height={30} />
      <Box height={30} />
      <Skeleton variant="rectangular" width="20%" height={40} />
      <Box sx={{ display: 'flex', mt: 3 }}>
        <Box sx={{ width: '20%', mr: 2 }}>
          <Skeleton variant="rectangular" width="100%" height={40} />
        </Box>
        <Box sx={{ width: '80%' }}>
          <Skeleton variant="rectangular" width="100%" height={40} />
        </Box>
      </Box>
      <Box sx={{ display: 'flex', mt: 3 }}>
        <Box sx={{ width: '50%', mr: 2 }}>
          <Skeleton variant="rectangular" width="100%" height={40} />
        </Box>
        <Box sx={{ width: '50%' }}>
          <Skeleton variant="rectangular" width="100%" height={40} />
        </Box>
      </Box>
      <Box sx={{ display: 'flex', mt: 3 }}>
        <Box sx={{ width: '40%', mr: 2 }}>
          <Skeleton variant="rectangular" width="100%" height={40} />
        </Box>
        <Box sx={{ width: '60%' }}>
          <Skeleton variant="rectangular" width="100%" height={40} />
        </Box>
      </Box>
      <Box sx={{ mt: 3 }}>
        <Skeleton variant="rectangular" width="100%" height={400} />
      </Box>
    </Box>
  );
};

export default SkeletonLoader;
