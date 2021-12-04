import { logger } from '../shared/logger';

const parseList = response => {
  if (response.status !== 200) logger.error(response.message);
  if (!response.data) return [];
  let list = response.data;
  if (typeof list !== 'object') {
    list = [];
  }
  return list;
};

const parseItem = response => {
  if (response.status < 200 || response.status >= 300) logger.error(response.message);
  let item = response.data;
  if (typeof item == 'undefined') {
    item = undefined;
  }
  return item;
};

export const serviceTools = {
  parseList, 
  parseItem
};
