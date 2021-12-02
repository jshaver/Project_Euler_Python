import * as axios from 'axios';
import { format } from 'date-fns';
import { API } from '../shared/config';
import { logger } from '../shared/logger';
import { inputDateFormat } from '../shared/constants';
import { serviceTools } from './service_tools';


const getProblems = async function(){
  try{
    const response = await axios.get(`${API}/problems`);
    let data = serviceTools.parseList(response);
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
    let data = serviceTools.parseItem(response);
    return data;
  } catch(e){
    logger.error(e);
    return null;
  }
};

const updateProblem = async function(problem){
  try{
    const response = await axios.put(`${API}/problems/${problem.id}`, problem);
    const updatedProblem = serviceTools.parseItem(response);
    return updatedProblem;
  } catch (e){
    console.error(e);
    return null;
  }
};

const createSolution = async function(solution){
  try{
    const response = await axios.post(`${API}/solutions`, solution);
    const newSolution = serviceTools.parseItem(response);
    return newSolution;
  } catch (e) {
    logger.error(e);
    return [];
  }
};

const getSolutions = async function(){
  try{
    const response = await axios.get(`${API}/solutions`);
    let data = serviceTools.parseList(response);
    const solutionData = data.map(s => {
      s.solutionDate = format(s.solutionDate, inputDateFormat);
      return s;
    });
    //logger.info('getSolutions success', data);
    logger.info('getSolutions success');
    return solutionData;
  } catch(e) {
    logger.error(e);
    return [];
  }
};

const getSolution = async function(id){
  try{
    const response = await axios.get(`${API}/solutions/${id}`);
    let data = serviceTools.parseItem(response);
    data.dateSolved = format(data.dateSolved, inputDateFormat);
    return data;
  } catch(e){
    logger.error(e);
    return null;
  }
};

const updateSolution = async function(solution){
  try{
    const response = await axios.put(`${API}/solutions/${solution.id}`, solution);
    const updatedSolution = serviceTools.parseItem(response);
    return updatedSolution;
  } catch (e){
    console.error(e);
    return null;
  }
};

const deleteSolution = async function(id){
  try{
    const response = await axios.delete(`${API}/solutions/${id}`);
    const deletedSolution = serviceTools.parseItem(response);
    return deletedSolution;
  } catch(e){
    logger.error(e);
    return null;
  }
};


export const dataService = {
  //createProblem,
  getProblems, 
  getProblem, 
  updateProblem,
  //deleteProblem,
  createSolution,
  getSolutions, 
  getSolution,
  updateSolution, 
  deleteSolution
};
