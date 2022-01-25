from pydantic import BaseModel, Field
from typing import Literal


###############################################################################
# Submodels
###############################################################################


class PCA(BaseModel):
    pass


class TSNE(BaseModel):
    perplexity: int = Field(ge=5, le=50)
    iterations: int = Field(ge=250, le=5000)
    learning_rate: int = Field(ge=10, le=1000)
    metric: Literal['euclidean', 'cosine', 'minkowski',
                    'manhattan', 'chebyshev', 'canberra', 'mahalanobis']
    init: Literal['random', 'pca']


class UMAP(BaseModel):
    neighbors: int = Field(ge=2, le=200)
    min_distance: float = Field(ge=0.01, le=0.99)
    metric: Literal['euclidean', 'cosine', 'minkowski',
                    'manhattan', 'chebyshev', 'canberra', 'mahalanobis']
    densmap: bool


class TruncatedSVD(BaseModel):
    pass


class SpectralEmbedding(BaseModel):
    affinity: Literal['nearest_neighbors', 'rbf']


class Isomap(BaseModel):
    neighbors: int = Field(ge=2, le=200)
    metric: Literal['euclidean', 'cosine', 'minkowski',
                    'manhattan', 'chebyshev', 'canberra', 'mahalanobis']


class MDS(BaseModel):
    pass


###############################################################################
# Models
###############################################################################


class PCAModel(BaseModel):
    algorithm: Literal['pca']
    components: int = Field(ge=2, le=3)
    params: PCA


class TSNEModel(BaseModel):
    algorithm: Literal['tsne']
    components: int = Field(ge=2, le=3)
    params: TSNE


class UMAPModel(BaseModel):
    algorithm: Literal['umap']
    components: int = Field(ge=2, le=3)
    params: UMAP


class TruncatedSVDModel(BaseModel):
    algorithm: Literal['truncated_svd']
    components: int = Field(ge=2, le=3)
    params: TruncatedSVD


class SpectralEmbeddingModel(BaseModel):
    algorithm: Literal['spectral_embedding']
    components: int = Field(ge=2, le=3)
    params: SpectralEmbedding


class IsomapModel(BaseModel):
    algorithm: Literal['isomap']
    components: int = Field(ge=2, le=3)
    params: Isomap


class MDSModel(BaseModel):
    algorithm: Literal['mds']
    components: int = Field(ge=2, le=3)
    params: MDS
