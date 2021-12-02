import * as axios from 'axios';
import { API } from '../shared/config';
import { logger } from '../shared/logger';
import { serviceTools } from './service_tools';


const solveProblem001 = async function(inputParam){
  try{
    const response = await axios.get(`http://localhost:5000/problems?limit=10`);
    let data = serviceTools.parseItem(response);
    return data;
  } catch(e) {
    logger.error(e);
    return [];
  }
};


export const pythonService = {
  solveProblem001
};
