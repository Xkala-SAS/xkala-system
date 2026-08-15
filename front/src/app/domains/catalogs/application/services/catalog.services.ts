import { Injectable, inject } from '@angular/core';

import { CatalogHttpRepository } from '../../infrastructure/repositories/catalog-http.repository';

@Injectable({
  providedIn: 'root',
})
export class CatalogService {
  private repository = inject(CatalogHttpRepository);

  getDocumentTypes() {
    return this.repository.getDocumentTypes();
  }

  // futuro

  // getCities()
  // getEps()
  // getArls()
  // getPositions()
  // getContractTypes()
}
