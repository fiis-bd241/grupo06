import React, { useState } from 'react';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Collapse from '@mui/material/Collapse';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import List from '@mui/material/List';

const SubMenuItem = ({ subItem, navigate, open, currentPath }) => {
  const [subSubOpen, setSubSubOpen] = useState(false);

  const handleSubClick = () => {
    if (subItem.subItems && subItem.subItems.length > 0) {
      setSubSubOpen(!subSubOpen);
    } else {
      navigate(subItem.path);
    }
  };

  const isSubItemActive = currentPath === subItem.path || (subItem.subItems && subItem.subItems.some(subSubItem => currentPath === subSubItem.path));

  return (
    <>
      <ListItem disablePadding sx={{ display: 'block' }} onClick={handleSubClick}>
        <ListItemButton
          sx={{
            maxHeight: 32,
            justifyContent: open ? 'initial' : 'center',
            px: 4,
            fontSize: '8px',
            color: isSubItemActive ? '#881C62' : '#555555',
            backgroundColor: isSubItemActive ? '#F4EDF2' : 'transparent',
            '&:hover': {
              backgroundColor: '#F4EDF2',
            }
          }}
        >
          <ListItemText primary={subItem.text} sx={{ opacity: open ? 1 : 0 }} />
          {subItem.subItems && subItem.subItems.length > 0 ? (subSubOpen ? <ExpandLess /> : <ExpandMore />) : null}
        </ListItemButton>
      </ListItem>
      {subItem.subItems && subItem.subItems.length > 0 && (
        <Collapse in={subSubOpen} timeout="auto" unmountOnExit>
          <List component="div" disablePadding>
            {subItem.subItems.map((subSubItem, subSubIndex) => (
              <ListItem key={subSubIndex} disablePadding sx={{ pl: 4 }} onClick={(e) => {
                e.stopPropagation();
                navigate(subSubItem.path);
              }}>
                <ListItemButton
                  sx={{
                    maxHeight: 28,
                    justifyContent: open ? 'initial' : 'center',
                    px: 4,
                    fontSize: '10px',
                    color: currentPath === subSubItem.path ? '#881C62' : '#555555',
                    backgroundColor: currentPath === subSubItem.path ? '#F4EDF2' : 'transparent',
                    '&:hover': {
                      backgroundColor: '#F4EDF2',
                    }
                  }}
                >
                  <ListItemText primary={subSubItem.text} sx={{ opacity: open ? 1 : 0 }} />
                </ListItemButton>
              </ListItem>
            ))}
          </List>
        </Collapse>
      )}
    </>
  );
};

export default function MenuItem({ item, navigate, open, currentPath }) {
  const [subOpen, setSubOpen] = useState(false);

  const handleClick = () => {
    if (item.subItems && item.subItems.length > 0) {
      setSubOpen(!subOpen);
    } else {
      navigate(item.path);
    }
  };

  const isActive = currentPath === item.path || (item.subItems && item.subItems.some(subItem => currentPath === subItem.path));

  return (
    <>
      <ListItem disablePadding sx={{ display: 'block' }} onClick={handleClick}>
        <ListItemButton
          sx={{
            minHeight: 40,
            justifyContent: open ? 'initial' : 'center',
            px: 2.5,
            fontWeight: 'bold',
            fontSize: '14px',
            color: isActive ? '#881C62' : '#000',
            backgroundColor: isActive ? '#F4EDF2' : 'transparent',
            '&:hover': {
              backgroundColor: '#F4EDF2',
            }
          }}
        >
          <ListItemIcon
            sx={{
              minWidth: 0,
              mr: open ? 3 : 'auto',
              justifyContent: 'center',
              color: 'inherit',
            }}
          >
            {item.icon}
          </ListItemIcon>
          <ListItemText primary={item.text} sx={{ opacity: open ? 1 : 0 }} />
          {item.subItems && item.subItems.length > 0 ? (subOpen ? <ExpandLess /> : <ExpandMore />) : null}
        </ListItemButton>
      </ListItem>
      {item.subItems && item.subItems.length > 0 && (
        <Collapse in={subOpen} timeout="auto" unmountOnExit>
          <List component="div" disablePadding>
            {item.subItems.map((subItem, subIndex) => (
              <SubMenuItem 
                key={subIndex} 
                subItem={subItem} 
                navigate={navigate} 
                open={open} 
                currentPath={currentPath} 
              />
            ))}
          </List>
        </Collapse>
      )}
    </>
  );
}
