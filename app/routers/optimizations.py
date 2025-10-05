from typing import List
from uuid import UUID

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.controller import OptimizationController
from app.models.enums.response import Response
from app.models.optimization.dto import *

# Create a new APIRouter instance for the optimizations
router = APIRouter()

# Create a new OptimizationController instance
controller: OptimizationController = OptimizationController()


@router.post("/optimizations", response_model=OptimizationOutputBaseDTO, summary='create optimization')
def post_optimization(optimization_input_dto: OptimizationInputDTO) -> JSONResponse | OptimizationOutputBaseDTO:
    try:
        return controller.create_optimization(optimization_input_dto)
    except RuntimeError as e:
        return JSONResponse(status_code=500, content={'message': str(e)})


@router.get("/optimizations", response_model=List[OptimizationOutputBaseDTO], summary='get all optimizations')
def get_optimizations() -> List[OptimizationOutputBaseDTO]:
    return controller.get_optimizations()


@router.get("/optimizations/{optimization_id}", response_model=OptimizationOutputDTO, summary='get a specific optimization')
def get_optimization(optimization_id: UUID) -> JSONResponse | OptimizationOutputDTO:
    optimization = controller.get_optimization(optimization_id)

    if not isinstance(optimization, OptimizationOutputDTO):
        return JSONResponse(status_code=optimization.value[0],
                            content={'message': optimization.format_message(optimization_id=optimization_id)})

    return optimization


@router.get("/optimizations/{optimization_id}/statistics", response_model=OptimizationOutputStatisticsDTO, summary='get statistics for optimization')
def get_optimization_statistics(optimization_id: UUID) -> JSONResponse | OptimizationOutputStatisticsDTO:
    optimization_statistics = controller.get_optimization_statistics(optimization_id)

    if not isinstance(optimization_statistics, OptimizationOutputStatisticsDTO):
        return JSONResponse(status_code=optimization_statistics.value[0],
                            content={'message': optimization_statistics.format_message(optimization_id=optimization_id)})

    return optimization_statistics


@router.get("/optimizations/{optimization_id}/result", response_model=OptimizationOutputResultDTO, summary='get result for optimization')
def get_optimization_result(optimization_id: UUID) -> JSONResponse | OptimizationOutputResultDTO:
    optimization_result = controller.get_optimization_result(optimization_id)

    if not isinstance(optimization_result, OptimizationOutputResultDTO):
        return JSONResponse(status_code=optimization_result.value[0],
                            content={'message': optimization_result.format_message(optimization_id=optimization_id)})

    return optimization_result


@router.put("/optimizations/{optimization_id}/start", response_model=OptimizationOutputBaseDTO, summary='start optimization asynchronously')
async def start_optimization(optimization_id: UUID) -> JSONResponse | OptimizationOutputBaseDTO:
    optimization = controller.start_optimization(optimization_id, async_run=True)

    if not isinstance(optimization, OptimizationOutputBaseDTO):
        return JSONResponse(status_code=optimization.value[0],
                            content={'message': optimization.format_message(optimization_id=optimization_id)})

    return optimization


@router.put("/optimizations/{optimization_id}/start/wait", response_model=OptimizationOutputBaseDTO, summary='start optimization synchronously')
def start_optimization_wait(optimization_id: UUID) -> JSONResponse | OptimizationOutputBaseDTO:
    optimization = controller.start_optimization(optimization_id, async_run=False)

    if not isinstance(optimization, OptimizationOutputBaseDTO):
        return JSONResponse(status_code=optimization.value[0],
                            content={'message': optimization.format_message(optimization_id=optimization_id)})

    return optimization


@router.put("/optimizations/{optimization_id}/abort", response_model=OptimizationOutputBaseDTO, summary='abort optimization')
def abort_optimization(optimization_id: UUID) -> JSONResponse | OptimizationOutputBaseDTO:
    optimization = controller.abort_optimization(optimization_id)

    if not isinstance(optimization, OptimizationOutputBaseDTO):
        return JSONResponse(status_code=optimization.value[0],
                            content={'message': optimization.format_message(optimization_id=optimization_id)})

    return optimization


@router.delete("/optimizations/{optimization_id}", summary='delete optimization')
def delete_optimization(optimization_id: UUID) -> JSONResponse:
    delete = controller.delete_optimization(optimization_id)

    return JSONResponse(status_code=delete.value[0],
                        content={'message': delete.format_message(optimization_id=optimization_id)})
