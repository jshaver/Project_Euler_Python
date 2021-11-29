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

const getProblem = async function(id){
  try{
    const response = await axios.get(`${API}/problems/${id}`);
    let data = parseItem(response);
    return data;
  } catch(e){
    logger.error(e);
    return null;
  }
}

const updateProblem = async function(problem){
  try{
    const response = await axios.put(`${API}/problems/${problem.id}`, problem);
    const updatedProblem = parseItem(response);
    return updatedProblem;
  } catch (e){
    console.error(e);
    return null;
  }
}

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

const getSolution = async function(id){
  try{
    const response = await axios.get(`${API}/solutions/${id}`);
    let data = parseItem(response);
    return data;
  } catch(e){
    logger.error(e);
    return null;
  }
}

const updateSolution = async function(solution){
  try{
    const response = await axios.put(`${API}/solutions/${solution.id}`, solution);
    const updatedSolution = parseItem(response);
    return updatedSolution;
  } catch (e){
    console.error(e);
    return null;
  }
}

const parseList = response => {
  if (response.status !== 200) logger.error(response.message);
  if (!response.data) return [];
  let list = response.data;
  if (typeof list !== 'object') {
    list = [];
  }
  return list;
};

export const parseItem = (response) => {
  if (response.status !== 200) throw Error(response.message);
  let item = response.data;
  if (typeof item !== 'object') {
    item = undefined;
  }
  return item;
};

export const dataService = {
  //createProblem,
  getProblems, 
  getProblem, 
  updateProblem,
  //deleteProblem,
  //createSolution,
  getSolutions, 
  getSolution,
  updateSolution, 
  //deleteSolution
}