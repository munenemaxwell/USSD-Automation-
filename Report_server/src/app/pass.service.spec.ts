import { TestBed, inject } from '@angular/core/testing';

import { PassService } from './pass.service';

describe('PassService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [PassService]
    });
  });

  it('should be created', inject([PassService], (service: PassService) => {
    expect(service).toBeTruthy();
  }));
});
