import axios from 'axios'
import type { TripPlanRequest,TripPlan } from '../types'

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
  timeout: 120000, // 2分钟超时
  headers: {
    'Content-Type': 'application/json'
  }
})