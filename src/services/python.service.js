import * as axios from 'axios';
import { API } from '../shared/config';
import { logger } from '../shared/logger';
import { serviceTools } from './service_tools';


const solveProblem = async function(problemNum, inputParam){
  try{
    const response = await axios.get(`http://localhost:5000/solve?problem=${problemNum}&input=${inputParam}`);
    let data = serviceTools.parseItem(response);
    return data;
  } catch(e) {
    logger.error(e);
    return [];
  }
};


export const pythonService = {
  solveProblem
};
