import * as axios from 'axios';
import { format } from 'date-fns';
import { API } from './config';
import { logger } from './logger';

const getProblems = async function(){
  try{
    const response = await axios.get(`${API}/problems`);
    let data = parseList(response);
    //logger.info('getProblems success', data);
    logger.info('getProblems success');
    return data;
  } catch(e) {
    logger.error(e);
    return [];
  }
};

const getSolutions = async function(){
  try{
    const response = await axios.get(`${API}/solutions`);
    let data = parseList(response);
    //logger.info('getSolutions success', data);
    logger.info('getSolutions success');
    return data;
  } catch(e) {
    logger.error(e);
    return [];
  }
};

const parseList = response => {
  if (response.status !== 200) logger.error(response.message);
  if (!response.data) return [];
  let list = response.data;
  if (typeof list !== 'object') {
    list = [];
  }
  return list;
};

export const dataService = {
  getProblems, 
  getSolutions
}